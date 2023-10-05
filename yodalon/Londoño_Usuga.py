import math

class Conversion3D:
    def __init__(self,x, y, z):
        self.x = float (x)
        self.y = float (y)
        self.z = float (z)
        
    @staticmethod
    def grados_a_radianes (grados):
        return math.radians(grados)
    @staticmethod
    def radianes_a_grados (radianes):
        return math.degrees(radianes)

    def rectangular_a_cilindrico(self):
        rc= math.sqrt(self.x**2 + self.y**2)
        theta = math.atan2(self.y,self.x)
        theta_final = math.degrees(theta)
        return rc, self.radianes_a_grados(theta_final), self.z

    def main():
        while True:
    
            opcion = int(input("Seleccione el sistema original de sus coordenadas: \n  \t 1| Rectangular \n \t 2| Cilíndrico \n  \t 3| Esferico \n"))

            if opcion == 1:
                while True:
                    opcion = int(input("Seleccione el sistema al que desea convertir: \n \t 1| Cilíndrico \n \t 2| Esferico \n"))
                    if opcion == 1: 
                        num_tuplas = int(input("Ingrese el número de tuplas de coordenadas a convertir: "))
                        for i in range(num_tuplas):
                            x, y, z = input(f"Tupla {i+1}: \n Ingrese x, y, z : ").split()
                            convertidor = Conversion3D(x, y, z)
                            rectangular_a_cilindrico()
                    
if __name__ == "__main__":
    main()
                
