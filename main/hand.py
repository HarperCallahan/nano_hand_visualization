import open3d as o3d

class Finger():
    def __init__(self,x,y,z,size):
        #create joint visualization
        self.base = o3d.geometry.TriangleMesh.create_sphere()
        self.middle = o3d.geometry.TriangleMesh.create_sphere()
        self.end = o3d.geometry.TriangleMesh.create_sphere()
        self.tip = o3d.geometry.TriangleMesh.create_sphere()
        #put joints in correct position and size
        self.base.scale(0.5,center =self.base.get_center())
        self.base.translate((x,y,z))
        self.middle.scale(0.5,center = self.middle.get_center())
        self.middle.translate(self.base.get_center() + (2*size,y,z))
        self.end.scale(0.5,self.end.get_center())
        self.end.translate(self.middle.get_center() + (2*size*size, y, z))
        self.tip.scale(0.5, self.tip.get_center())
        self.tip.translate(self.end.get_center() + (2*(size**3), y,z))
        #color
        self.base.paint_uniform_color([0,1,0])
        self.middle.paint_uniform_color([0,1,0])
        self.end.paint_uniform_color([0,1,0])
        self.tip.paint_uniform_color([1,0,0])
        #add lines connecting joints
        self.line_set = o3d.geometry.LineSet(
            points = o3d.utility.Vector3dVector([self.base.get_center(), self.middle.get_center(), self.end.get_center(),self.tip.get_center()]), 
            lines = o3d.utility.Vector2iVector([[0,1],[1,2],[2,3]]))

    def draw(self,vis):
        vis.add_geometry(self.base)
        vis.add_geometry(self.middle)
        vis.add_geometry(self.end)
        vis.add_geometry(self.tip)
        vis.add_geometry(self.line_set)
    def update(self,vis):
        vis.update_geometry(self.base)
        vis.update_geometry(self.middle)
        vis.update_geometry(self.end)
        vis.update_geometry(self.tip)
        vis.update_geometry(self.line_set)
    
    def rotate(self, section, theta):
        if (section == "base"):
            self.middle.rotate(self.middle.get_rotation_matrix_from_xyz(theta) ,center = self.base.get_center())
            self.end.rotate(self.end.get_rotation_matrix_from_xyz(theta), center= self.base.get_center())
            self.tip.rotate(self.tip.get_rotation_matrix_from_xyz(theta),center= self.base.get_center())
        elif(section == "middle"):
            self.end.rotate(self.end.get_rotation_matrix_from_xyz(theta), center= self.middle.get_center())
            self.tip.rotate(self.tip.get_rotation_matrix_from_xyz(theta),center= self.middle.get_center())
        else:
            self.tip.rotate(self.tip.get_rotation_matrix_from_xyz(theta),center = self.end.get_center())
        self.line_set = o3d.geometry.LineSet(
            points = o3d.utility.Vector3dVector([self.base.get_center(), self.middle.get_center(), self.end.get_center(),self.tip.get_center()]), 
            lines = o3d.utility.Vector2iVector([[0,1],[1,2],[2,3]]))



