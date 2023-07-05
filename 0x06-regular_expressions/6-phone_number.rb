#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern '^h.n$' in the provided argument
matches = ARGV[0].scan(/^h.n$/)
puts matches.join
