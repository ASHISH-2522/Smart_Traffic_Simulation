import math

class ObjectTracker:
    def __init__(self):
        self.object_centers = {}
        self.next_id = 0
    
    def update_positions(self, detected_objects):
        tracked_objects = []
        
        for rect in detected_objects:
            x, y, w, h = rect
            center_x = (x + x + w) // 2
            center_y = (y + y + h) // 2
            
            # Find matching existing object
            match_found = False
            for obj_id, position in self.object_centers.items():
                distance = math.hypot(center_x - position[0], center_y - position[1])
                
                if distance < 35:
                    self.object_centers[obj_id] = (center_x, center_y)
                    tracked_objects.append([x, y, w, h, obj_id])
                    match_found = True
                    break
            
            # Assign new ID for new objects
            if not match_found:
                self.object_centers[self.next_id] = (center_x, center_y)
                tracked_objects.append([x, y, w, h, self.next_id])
                self.next_id += 1
        
        # Cleanup unused IDs
        active_centers = {}
        for obj_data in tracked_objects:
            _, _, _, _, obj_id = obj_data
            center = self.object_centers[obj_id]
            active_centers[obj_id] = center
        
        self.object_centers = active_centers
        return tracked_objects