class UndoRedo:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def perform_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()

    def show_active_page(self):
        return self.undo_stack[-1]

    def undo(self):
        if self.undo:
            last_action = self.undo_stack.pop()
            self.redo_stack.append(last_action)
            return last_action
        else:
            return None

    def redo(self):
        if self.redo:
            last_action = self.redo_stack.pop()
            self.undo_stack.append(last_action)
            return last_action
        else:
            return None


if __name__ == "__main__":
    browser = UndoRedo()

    browser.perform_action("kaggle.com")
    print("Click Active: ", browser.show_active_page())
    browser.perform_action("competitions")
    print("Click Active: ", browser.show_active_page())
    browser.perform_action("godaddy - forecasting")
    print("Click Active: ", browser.show_active_page())

    browser.undo()
    print("Undo Active: ", browser.show_active_page())
    browser.undo()
    print("Undo Active: ", browser.show_active_page())
    browser.redo()
    print("Redo Active: ", browser.show_active_page())

    browser.perform_action("code")
    print("Click Active: ", browser.show_active_page())
    browser.perform_action("learn")
    print("Click Active: ", browser.show_active_page())

    browser.undo()
    print("Undo Active: ", browser.show_active_page())
