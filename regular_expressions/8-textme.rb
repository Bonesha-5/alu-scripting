#!/usr/bin/env ruby
# Extracts [SENDER],[RECEIVER],[FLAGS] from TextMe logs

input = ARGV[0]

# Regex to capture [from:...], [to:...], [flags:...]
match = input.match(/\[from:(?<from>.*?)\] \[to:(?<to>.*?)\] \[flags:(?<flags>.*?)\]/)

if match
  puts "#{match[:from]},#{match[:to]},#{match[:flags]}"
end
