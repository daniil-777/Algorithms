class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        rooms_visited = set()
        def visit(num_room):
            rooms_visited.add(num_room)
            if len(rooms[num_room]) != 0:
                for num in rooms[num_room]:
                     if num not in rooms_visited:    
                            visit(num)  
#             if num_room not in rooms_visited and len(rooms[num_room]) != 0:
                
#                 for num in rooms[num_room]:
                    
#                     visit(num)
                
        visit(0)
        print("rooms_visited: ", rooms_visited)
        if len(rooms_visited) == len(rooms):
            return True
        else:
            return False