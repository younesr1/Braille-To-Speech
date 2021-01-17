#!/usr/bin/julia

include("vis.jl")

img_name = ARGS[1]
out_name = ARGS[2]

braille_chars = image_to_braille(img_name)

io = open(out_name,"w")

for word in braille_chars
	for char in word
		for c in transpose(char)
			write(io, string(c))
			write(io, ",")
		end
		write(io,"\n")
	end
end

close(io)
