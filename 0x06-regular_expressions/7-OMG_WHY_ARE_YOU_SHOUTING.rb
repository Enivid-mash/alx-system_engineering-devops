#!/usr/bin/env ruby
# Ruby script using Oniguruma for regular expression matching

# Print the matches of the pattern '[A-Z]*' in the provided argument
matches = ARGV[0].scan(/[A-Z]*/)
puts matches.join
