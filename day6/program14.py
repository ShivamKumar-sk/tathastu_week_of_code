n=4
def rotate(mat): 

	for x in range(0, int(n / 2)): 

		for y in range(x, n-x-1): 
			temp = mat[x][y] 
			mat[x][y] = mat[y][n-1-x] 
			mat[y][n-1-x] = mat[n-1-x][n-1-y] 
			mat[n-1-x][n-1-y] = mat[n-1-y][x] 
			mat[n-1-y][x] = temp 

def displayMatrix( mat ): 
	
	for i in range(0, n): 
		
		for j in range(0, n): 
			
			print (mat[i][j], end = ' ') 
		print ("") 
	
	



mat = [[0 for x in range(n)] for y in range(n)] 


mat = [ [1, 2, 3, 4 ], 
	[5, 6, 7, 8 ], 
	[9, 10, 11, 12 ], 
	[13, 14, 15, 16 ] ] 
		
rotate(mat) 
displayMatrix(mat) 



