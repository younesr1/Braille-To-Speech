using SparseArrays, LinearAlgebra, Images, ImageView

# Converts img to greyscale matrix representation of the image
#
# returns: mxn Float64 array
function img_to_array(img_name)
	img = load(img_name)
	img = Gray.(img)
	return convert(Array{Float64,2}, img)
end

# Used to keep pixel intensity sums lower
switcheroo(x) = x = 1-x

# Partitions image into num_cols * num_rows rectangles and returns the
# the partitions as t_images and the sum of the region's pixel intensity
# as sums
function get_regions(img,s,num_cols=2,num_rows=3)
	# initialize returned values
	sums = Float64[]	
	t_images = []
 
	for col in 1:num_cols
		for row in 1:num_rows
			# Reference the (col * row)th partition of img
			region = @view img[max(1,Int(round((row-1)*s[1]/num_rows))):Int(round(row*s[1]/num_rows)), 
												max(1,Int(round((col-1)*s[2]/num_cols))):Int(round(col*s[2]/num_cols))]
			 
			t = map(switcheroo,region)
			push!(t_images,t)
			
			push!(sums, norm(t)) 
		end
	end
	
	return sums, t_images
end

# Take the sums matrix and output a matrix that represents the
# braille representation
function get_output_vector(sums)
	largest = maximum(sums)
	tolerance = largest/4	
	vect = [ abs(largest - sum) < tolerance for sum in sums] 
	return Int.(reshape(vect,3,2))
end 

# Given an imageof a single char we return the regions of the
# image, the sums of those regions and the output vector
#
# ** Output of t_images and sums is for testing purposes
function process_char(img)
	s = size(img)
	sums, t_images = get_regions(img,s)
	output_vector = get_output_vector(sums)
	return sums, t_images, output_vector
end

# Preliminary version of processing the image to feed the
# single characters to the process_char function
#
# ** Output of chars is for testing purposes
function process_chars(img,s,num_chars)
	chars = [ @view img[:,max(1,Int(round((col-1)*s[2]/num_chars))):Int(round(col*s[2]/num_chars))]
						for col in 1:num_chars ]
	
	outputs = [ process_char(char) for char in chars ]

	return chars, outputs
end


function image_to_braille(img_name, num_chars)
	img = img_to_array(img_name)
	s = size(img)
	chars, outputs = process_chars(img, s, num_chars)
	imshow(img)
	return [output[3] for output in outputs]
end





