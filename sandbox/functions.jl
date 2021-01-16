using SparseArrays, LinearAlgebra, Images, ImageView

function img_to_array(img_name)
	img = load(img_name)
	img = Gray.(img)
	return convert(Array{Float64,2}, img)
end


ops(x) = x = 1-x

function get_regions(img,s,num_cols=2,num_rows=3)
	sums = Float64[]	
	t_images = [] 
	for col in 1:num_cols
		for row in 1:num_rows
			region = @view img[max(1,Int(round((row-1)*s[1]/num_rows))):Int(round(row*s[1]/num_rows)), 
												max(1,Int(round((col-1)*s[2]/num_cols))):Int(round(col*s[2]/num_cols))]
			t = map(ops,region)
			push!(t_images,t)
			push!(sums, norm(t)) 
		end
	end
	return sums, t_images
end

function get_output_vector(sums)
	largest = maximum(sums)
	tolerance = 3 	
	vect = [ abs(largest - sum) < tolerance for sum in sums] 
	return Int.(reshape(vect,3,2))
end 

function process_char(img)
	s = size(img)
	sums, t_images = get_regions(img,s)
	output_vector = get_output_vector(sums)
	return sums, t_images, output_vector
end

function process_chars(img,s,num_chars)
	chars = [ @view img[:,max(1,Int(round((col-1)*s[2]/num_chars))):Int(round(col*s[2]/num_chars))]
						for col in 1:num_chars ]
	
	outputs = [ process_char(char) for char in chars ]

	return chars, outputs
end



