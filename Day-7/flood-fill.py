class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        
        def flood_fill(i, j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]): return
            
            if image[i][j] == color: return
            if image[i][j] != start_color: return
            
            image[i][j] = 3
    
            flood_fill(i-1, j)
            flood_fill(i, j-1)
            flood_fill(i+1, j)
            flood_fill(i, j+1)
            
        flood_fill(sc, rc)
        return image
    