#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern 'hb?t?n' in the provided argument
matches = ARGV[0].scan(/hb?t?n/)
puts matches.join
