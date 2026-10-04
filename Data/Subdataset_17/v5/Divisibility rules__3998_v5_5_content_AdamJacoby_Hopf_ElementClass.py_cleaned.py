import numpy as np
from HopfClass import *
class VectorSpaceElement:
    def __init__(self, vector, space):
        self.space = space
        self.vector = self._parse_vector(vector)
        self.name = 'Currently unnamed.'
    def _parse_vector(self, vector):
        if isinstance(vector, str):
            if vector == '0':
                return np.zeros(self.space.dim, dtype=complex)
            else:
                vec = np.zeros(self.space.dim, dtype=complex)
                terms = vector.split('+')
                for term in terms:
                    coefficient, name = term.split('*')
                    if name in self.space.element_names:
                        index = self.space.element_names.index(name)
                        vec[index] = complex(coefficient)
                return vec
        return vector
    def tensor(self, other):
        out_type = self._determine_output_type(other)
        out_vector = self._compute_tensor_product(other)
        element_class = globals().get(f'{out_type}Element')
        return element_class(out_vector, AlgebraList[f'{self.space.name}(T){other.space.name}'])
    def _determine_output_type(self, other):
        if self.space.type == 'HopfAlgebra' and other.space.type == 'HopfAlgebra':
            return 'HopfAlgebra'
        elif self.space.type == 'Algebra' or other.space.type == 'Algebra':
            return 'Algebra'
        elif (self.space.type in ['ModuleAlgebra', 'HopfAlgebra'] and
              other.space.type in ['ModuleAlgebra', 'HopfAlgebra']):
            return 'ModuleAlgebra'
        return 'VectorSpace'
    def _compute_tensor_product(self, other):
        out_vector = np.zeros(self.space.dim * other.space.dim, dtype=complex)
        for i in range(self.space.dim):
            for j in range(other.space.dim):
                out_vector[i * other.space.dim + j] = self.vector[i] * other.vector[j]
        return out_vector
    def __add__(self, other):
        element_class = globals().get(f'{self.space.type}Element')
        return element_class(self.vector + other.vector, self.space)
    def __sub__(self, other):
        element_class = globals().get(f'{self.space.type}Element')
        return element_class(self.vector - other.vector, self.space)
    def name(self):
        if self.name == 'Currently unnamed.':
            parts = [f'{self.vector[i]}*{self.space.element_names[i]}'
                     for i in range(self.space.dim) if self.vector[i] != 0]
            self.name = '+'.join(parts) if parts else '0'
        return self.name
class AlgebraElement(VectorSpaceElement):
    def __mul__(self, other):
        if isinstance(other, (complex, int, float, np.complex128)):
            element_class = globals().get(f'{self.space.type}Element')
            return element_class(other * self.vector, self.space)
        elif self.space == other.space:
            result_vector = self.space.multiply(self.vector, other.vector)
            element_class = globals().get(f'{self.space.type}Element')
            return element_class(result_vector, self.space)
        elif other.space.type in ['Module', 'ModuleAlgebra']:
            action_result = other.space.action(self.vector, other.vector)
            return ModuleAlgebraElement(action_result, other.space)
    def __pow__(self, power):
        result = self
        if power == 0:
            temp = np.zeros(self.vector.shape[0])
            temp[0] = 1
            element_class = globals().get(f'{self.space.type}Element')
            return element_class(temp, self.space)
        for _ in range(power - 1):
            result *= self
        return result
class CoAlgebraElement(VectorSpaceElement):
    def comultiplication(self):
        if self.space.type == 'CoAlgebra':
            result_vector = self.space.comultiplication(self.vector)
            return CoAlgebraElement(result_vector, AlgebraList[f'{self.space.name}(T){self.space.name}'])
        elif self.space.type == 'HopfAlgebra':
            result_vector = self.space.comultiplication(self.vector)
            return HopfAlgebraElement(result_vector, AlgebraList[f'{self.space.name}(T){self.space.name}'])
    def counit(self):
        return self.space.counit(self.vector)
class HopfAlgebraElement(AlgebraElement, CoAlgebraElement):
    def antipode(self):
        return HopfAlgebraElement(self.space.antipode(self.vector), self.space)
class ModuleElement(VectorSpaceElement):
    def act(self, ring_element):
        vector = self.space.action(ring_element.vector, self.vector)
        element_class = globals().get(f'{self.space.type}Element')
        return element_class(vector, self.space)
class ModuleAlgebraElement(ModuleElement, AlgebraElement):
    def smash(self, other):
        vector = ProdVectorToTensorVector(self.vector, other.vector)
        return ModuleAlgebraElement(vector, AlgebraList[f'{self.space.name}{other.space.name}'])
if __name__ == '__main__':
    pass