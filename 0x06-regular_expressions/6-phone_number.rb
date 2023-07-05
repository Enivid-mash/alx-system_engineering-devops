#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern '^\d{10,10}$' in the provided argument
matches = ARGV[0].scan(/^\d{10,10}$/)
puts matches.join
