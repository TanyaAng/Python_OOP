class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def find_category_by_id(self, id):
        category = [c for c in self.categories if c.id == id]
        if category:
            return category[0]

    def find_topic_by_id(self, id):
        topic = [t for t in self.topics if t.id == id]
        if topic:
            return topic[0]

    def find_document_by_id(self, id):
        document = [d for d in self.documents if d.id == id]
        if document:
            return document[0]

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.find_category_by_id(category_id)
        if category:
            category.name = new_name

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.find_topic_by_id(topic_id)
        if topic:
            topic.topic = new_topic
            topic.storage_folder = new_storage_folder

    def edit_document(self, document_id, new_file_name):
        document = self.find_document_by_id(document_id)
        if document:
            document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.find_category_by_id(category_id)
        if category:
            self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_topic_by_id(topic_id)
        if topic:
            self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_document_by_id(document_id)
        if document:
            self.documents.remove(document)

    def get_document(self, document_id):
        return self.find_document_by_id(document_id)

    def __repr__(self):
        result = ''
        for d in self.documents:
            result += repr(d) + '\n'
        return result


from project.category import Category
from project.document import Document
# from project.storage import Storage
from project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)


