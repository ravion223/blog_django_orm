import django_setup

from blog.models import Publication, Commentary


def add_publication(title, content):
    publication = Publication(
        title = title,
        content = content
    )

    publication.save()

    return publication

def add_commentary_to_publication(text, author, publication_id):
    commentary = Commentary(
        text = text,
        author = author
    )
    
    commentary.save()

    publication = Publication.objects.get(id = publication_id)
    publication.commentaries.add(commentary)

    return publication.commentaries


def main():
    while True:
        request = int(input("Publish publication - 1\nLeave a comment to publication - 2\nExit - 0\n"))

        match request:
            case 1:
                title = input("Title: ")
                content = input("Content: ")
                print(add_publication(title, content))

            case 2:
                text = input("Text: ")
                author = input("Author: ")
                publication_id = int(input("Publication id: "))
                print(add_commentary_to_publication(text, author, publication_id))


if __name__ == "__main__":
    main()