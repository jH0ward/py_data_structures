class BinaryHeap:
    def __init__(self):
        self._array = []

    @classmethod
    def create_heap(cls, values):
        heap = cls()
        heap._heapify(values)
        return heap

    def _heapify(self, values):
        self._array = values
        i = len(values) // 2
        while i > -1:
            self._sift_down(i)
            i -= 1

    def insert(self, value):
        next_index = len(self._array)
        #self._array[next_index] = value
        self._array.append(value)
        self._sift_up(next_index)

    def _sift_up(self, i):
        parent_index = self._get_parent_index(i)
        print("called sift up for i = ",i)
        print("array = ", self._array)
        while i > 0 and self._array[i] > self._array[parent_index]:
            temp = self._array[i]
            self._array[i] = self._array[parent_index]
            self._array[parent_index] = temp
            i = parent_index
            parent_index = self._get_parent(i)

    def _sift_down(self, i):
        max_index = i
        left_child_index = self._get_left_child_index(i)
        right_child_index = self._get_right_child_index(i)
        #print("i = ", i)
        #print("left child = ", left_child_index)
        #print("right child = ", right_child_index)

        # Check left child
        if left_child_index < len(self._array) and self._array[left_child_index] > self._array[max_index]:
            #self._array[left_child_index], self._array[max_index] = self._array[max_index], \
            #                                                        self._array[left_child_index]
            max_index = left_child_index

        # Check right child
        if right_child_index < len(self._array) and self._array[right_child_index] > self._array[max_index]:
            #self._array[right_child_index], self._array[max_index] = self._array[max_index], \
            #                                                        self._array[right_child_index]
            max_index = right_child_index
        #print("THe max index was = ", max_index)
        if i == max_index:
            return
        else:
            self._array[i], self._array[max_index] = self._array[max_index], self._array[i]
            self._sift_down(max_index)

    def _pop(self):
        max_val = self.get_max()
        print("Array before pop = ", self._array)
        self._array[0] = self._array.pop()
        self._sift_down(0)
        return max_val

    def get_max(self):
        if self._array:
            return self._array[0]
        else:
            return None

    def get_sorted_array(self):
        sorted_list = []
        for i in range(len(self._array)-1):
            sorted_list.append(self._pop())
        sorted_list.append(self._array[0])
        return sorted_list

    def _get_parent(self, child_idx):
        if child_idx == 0:
            return None
        parent_idx = self._get_parent_index(child_idx)
        return self._array[parent_idx]

    def __repr__(self):
        s = ""
        s += "[ "
        for val in self._array:
            s += str(val) + " "
        s += "]"
        return s

    def in_place_sort(self):
        new_array = []
        n = len(self._array)
        for i in range(n-1):
            print("swapping ", self._array[0]," and ", self._array[n-1])
            self._array[0], self._array[n-1] = self._array[n-1], self._array[0]
            new_array.append(self._array.pop())
            self._sift_down(0)
            print("New array: ", self._array)
            n -= 1
        #return self._array
        return new_array

    @staticmethod
    def _get_parent_index(child_idx):
        return int(child_idx+1/2) - 1

    @staticmethod
    def _get_left_child_index(parent_idx):
        #return (parent_idx+1)*2-1 # == 2*pidx +1
        return 2*parent_idx + 1

    @staticmethod
    def _get_right_child_index(parent_idx):
        return 2*parent_idx + 2


if __name__ == '__main__':
    input_values = [1, 9, 5, 6, 2, 3, 14, 3]
    max_heap = BinaryHeap.create_heap(input_values)
    print(max_heap)

    max_heap = BinaryHeap.create_heap(input_values)
    print(max_heap._array)
    #sorted_array = max_heap.get_sorted_array()
    #print(sorted_array)

    sorted_array = max_heap.in_place_sort()
    print(sorted_array)


