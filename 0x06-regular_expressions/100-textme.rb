#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern '\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]' in the provided argument
matches = ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/)
puts matches.join(",")
