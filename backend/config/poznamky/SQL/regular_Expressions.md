## .
Matches any single character except a newline.
`a.b matches "acb", "a1b"`
## ^	
Asserts position at the start of a string.
`^abc matches "abc" in "abcxyz"`
## $
Asserts position at the end of a string.
`xyz$ matches "xyz" in "abcxyz"`
## *	
Matches zero or more occurrences of the preceding element.
`a* matches "", "a", "aa", etc`
## +
Matches one or more occurrences of the preceding element.
`a+ matches "a", "aa", "aaa"`
## ?
Matches zero or one occurrence of the preceding element.
`a? matches "", "a"`
## {n}
Matches exactly n occurrences of the preceding element.
`a{3} matches "aaa"`
## {n,}
Matches n or more occurrences of the preceding element.
`a{2,} matches "aa", "aaa"`
## {n,m}
Matches between n and m occurrences of the preceding element.
`a{2,4} matches "aa", "aaa", or "aaaa"`
## [abc]
Matches any single character within the brackets (character class).
`[aeiou] matches any vowel`
## [^abc]
Matches any single character not in the brackets (negation).
`[^aeiou] matches any consonant`
## (abc)
Groups multiple characters together as a single unit (capturing group).
`(abc)+ matches "abcabc"`
## `
Acts as a logical OR between expressions.
## \d
Matches any digit (equivalent to [0-9]).
`\d{2} matches "12" in "123"`
## \D
Matches any non-digit character.
`\D+ matches non-digit sequences`
Matches any word character (alphanumeric plus underscore; equivalent to [A-Za-z0-9_]).
## \w
`\w+ matches words like "hello_123"`
## \W
Matches any non-word character.
`\W+ matches spaces and punctuation`
## \s
Matches any whitespace character (space, tab, newline).
`\s+ matches one or more spaces`
## \S
Matches any non-whitespace character.
`\S+ matches sequences without spaces`
