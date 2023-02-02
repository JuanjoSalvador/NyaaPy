class CategoryNotFound(Exception):
    
    def __init__(self, category: str, *args: object) -> None:
        super().__init__(*args)
        self.category = category

    def __str__(self) -> str:
        return f"Unable to get category name: {category}"
