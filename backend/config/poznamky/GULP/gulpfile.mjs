const gulp = require('gulp');
const ts = require('gulp-typescript');
const sass = require('gulp-sass')(require('sass'));
const autoprefixer = require('gulp-autoprefixer');
const cleanCSS = require('gulp-clean-css');
const terser = require('gulp-terser');
const sourcemaps = require('gulp-sourcemaps');

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
