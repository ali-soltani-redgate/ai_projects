from pathlib import Path

def main():
    docs_path = Path(__file__).parent / "documents"
    for doc in docs_path.glob("*.txt"):
        print(f"Reading document: {doc.name}")
        with open(doc, "r") as f:
            content = f.read()
            print(f"Content of {doc.name}:\n{content}\n")
    


if __name__ == "__main__":
    main()
