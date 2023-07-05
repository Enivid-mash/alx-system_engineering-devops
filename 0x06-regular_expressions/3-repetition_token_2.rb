#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern 'hbt+n' in the provided argument
matches = ARGV[0].scan(/hbt+n/)
puts matches.join
