import os
class DatasetClass:
    def __init__(self, required_no):
        dataset_name = "ORL"
        dir_path = os.path.join("images", dataset_name)
        self.image_path_for_training = []
        self.labels_for_training = []
        self.no_of_images_for_training = []
        self.image_path_for_testing = []
        self.labels_for_testing = []
        self.no_of_images_for_testing = []
        self.images_target = []
        per_no = 0
        for name in os.listdir(dir_path):
            subdir_path = os.path.join(dir_path, name)
            if os.path.isdir(subdir_path) and len(os.listdir(subdir_path)) >= required_no:
                i = 0
                for img_name in os.listdir(subdir_path):
                    img_path = os.path.join(subdir_path, img_name)
                    if i < required_no:
                        self.image_path_for_training.append(img_path)
                        self.labels_for_training.append(per_no)
                        if len(self.no_of_images_for_training) > per_no:
                            self.no_of_images_for_training[per_no] += 1
                        else:
                            self.no_of_images_for_training.append(1)
                        if i == 0:
                            self.images_target.append(name)
                    else:
                        self.image_path_for_testing.append(img_path)
                        self.labels_for_testing.append(per_no)
                        if len(self.no_of_images_for_testing) > per_no:
                            self.no_of_images_for_testing[per_no] += 1
                        else:
                            self.no_of_images_for_testing.append(1)
                    i += 1
                per_no += 1
