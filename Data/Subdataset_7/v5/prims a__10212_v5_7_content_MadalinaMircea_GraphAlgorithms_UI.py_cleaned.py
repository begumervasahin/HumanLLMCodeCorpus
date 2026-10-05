'''
Created on March 29, 2017
@author: Madalina
'''
class class1:
    def fonk1(self, b1):
        self.b1 = b1
    def fonk2(self):
        b2 = self.b1.find_hamiltonian_cycle()
        if not b2:
            print("No Hamiltonian cycles were found.")