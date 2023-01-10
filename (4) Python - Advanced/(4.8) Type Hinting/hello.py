# With type hinting
def is_eligible(platform: str, age: int) -> bool:
    if platform == "facebook" and age >= 13:
        return True
    if platform == "twitter" and age >= 18:
        return True

    return False


if __name__ == "__main__":
    platform: str = "facebook"
    age: int = 15
    print(is_eligible(platform, age))
