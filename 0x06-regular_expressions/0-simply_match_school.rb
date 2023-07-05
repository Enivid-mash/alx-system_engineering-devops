#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern 'School' in the provided argument
matches = ARGV[0].scan(/School/)
puts matches.join
