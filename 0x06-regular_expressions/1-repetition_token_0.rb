#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern 'hbt{2,5}n' in the provided argument
matches = ARGV[0].scan(/hbt{2,5}n/)
puts matches.join
