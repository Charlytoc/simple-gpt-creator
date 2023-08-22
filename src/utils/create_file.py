from typing import Optional
def create_file(path_dir: str = 'out', filename: Optional[str] = "file.txt", content: str = "") -> None:
        """
        Creates a file with the given filename and writes the content to it in the specified directory.
        Args:
                path_dir (str): The directory where the file will be created.
                filename (str, optional): The name of the file including the extension. Defaults to "file.txt".
                content (str): The content to be written in the file. Defaults to an empty string.
        Returns:
                None
        """
        file_path = path_dir + "/" + filename
        with open(file_path, "w", encoding='utf-8') as file:
                file.write(content)