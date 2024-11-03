import gulp from 'gulp';
import ts from 'gulp-typescript';
import * as _sass from 'sass'
import gulpSass from 'gulp-sass';

import autoprefixer from 'gulp-autoprefixer';
import cleanCSS from 'gulp-clean-css';
import terser from 'gulp-terser';
import sourcemaps from 'gulp-sourcemaps';

const sass = gulpSass(_sass);

// TypeScript project
const tsProject = ts.createProject('tsconfig.json');

// Transpile TypeScript
gulp.task('scripts', function () {
    return tsProject.src()
        .pipe(sourcemaps.init())
        .pipe(tsProject())
        .pipe(terser()) // Minify JavaScript
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('dist/js'));
});

// Compile SCSS
gulp.task('styles', function () {
    return gulp.src('src/scss/**/*.scss') // Adjust the path as needed
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(cleanCSS())
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest('dist/css'));
});

// Watch for changes
gulp.task('watch', function () {
    gulp.watch('src/ts/**/*.ts', gulp.series('scripts')); // Watch TypeScript files
    gulp.watch('src/scss/**/*.scss', gulp.series('styles')); // Watch SCSS files
});

// Default task
gulp.task('default', gulp.series(gulp.parallel('scripts', 'styles'), 'watch'));

