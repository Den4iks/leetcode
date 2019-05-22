# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
class quickSort():

    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):

            # If current element is smaller than or
            # equal to pivot
            if arr[j] <= pivot:
                # increment index of smaller element
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return (i + 1)


# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index

# Function to do Quick sort
    def quickSort(self, arr, low, high):
        if low < high:
            # pi is partitioning index, arr[p] is now
            # at right place
            pi = self.partition(arr, low, high)

            # Separately sort elements before
            # partition and after partition
            quickSort(arr, low, pi - 1)
            quickSort(arr, pi + 1, high)

        # Driver code to test above


class MergeSort():
    def split(self, list):
        if list is None:
            return None
        mid = len(list) // 2
        return list[:mid],list[mid:]


    def merger_sorgted_list(self, left_list, right_list):
        if len(left_list) == 0:
            return right_list
        elif len(right_list) == 0:
            return left_list

        left_list_index = right_list_index = 0
        merge_list = []
        merge_list_len = len(left_list) + len(right_list)

        while len(merge_list) < merge_list_len:
            if left_list[left_list_index] <= right_list[right_list_index]:
                merge_list.append(left_list[left_list_index])
                left_list_index += 1
            else:
                merge_list.append(right_list[right_list_index])
                right_list_index += 1

            if left_list_index == len(left_list):
                merge_list += right_list[right_list_index:]
            elif right_list_index == len(right_list):
                merge_list += left_list[left_list_index:]

        return merge_list

    def merge_sort(self,input_list):
        if len(input_list) <= 1:
            return input_list
        left,right = self.split(input_list)
        return self.merger_sorgted_list(self.merge_sort(left), self.merge_sort(right))


if __name__ == "__main__":
    arr = [10, 2, 8, 9, 1, 5]
    n = len(arr)
    sort = MergeSort()
    list = sort.merge_sort(arr)
    print("Sorted array is:")
    for i in range(n):
        print("%d" % arr[i]),

        # This code is contributed by Mohit Kumra