def get_book_text(path):
    with open(path) as f:
        return f.read()   
def main():
    book_path = "workspace/github.com/bootdotdev/bookbot_project/bookbot/books/frankenstein.txtx"
    text = get_book_text(book_path)
    print(text)
    
main()
        