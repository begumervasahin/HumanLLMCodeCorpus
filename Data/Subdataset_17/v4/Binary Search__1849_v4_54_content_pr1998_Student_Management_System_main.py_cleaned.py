import time
import bst
def get_student_details():
    roll_num = int(input("Enter the roll number: "))
    name = input("Enter the name: ")
    address = input("Enter the address: ")
    mobile = int(input("Enter the mobile number: "))
    course = input("Enter the course: ")
    print("Enter the marks in three subjects:")
    marks = [int(input(f"Subject {i + 1}: ")) for i in range(3)]
    total_marks = sum(marks)
    average_marks = total_marks / 3
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    return roll_num, name, address, mobile, course, total_marks, average_marks
def main():
    bst_tree = bst.BST()
    num_students = int(input("Enter the number of students: "))
    for i in range(num_students):
        print(f"\nEnter the details of Student {i + 1}:")
        student_details = get_student_details()
        bst_tree.insert(student_details[0])
    print("\nBST In-Order Traversal:\n")
    bst_tree.inorder()
    if input("Do you want to delete any keys in the tree? (y/n): ").lower() == 'y':
        while True:
            key_to_delete = int(input("Enter the roll number to delete: "))
            bst_tree.remove(key_to_delete)
            if input("Do you want to delete another key? (y/n): ").lower() != 'y':
                break
        print("\nAfter deletion, BST In-Order Traversal:\n")
        bst_tree.inorder()
    if input("Do you want to search any keys in the tree? (y/n): ").lower() == 'y':
        while True:
            key_to_search = int(input("Enter the roll number to search: "))
            bst_tree.search(key_to_search)
            if input("Do you want to search another key? (y/n): ").lower() != 'y':
                break
    print("\n************************* END OF BST OPERATIONS *******************************\n")
if __name__ == '__main__':
    main()