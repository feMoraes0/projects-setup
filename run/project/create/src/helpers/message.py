from colored import fg, attr

class Message:
  def success(self, message):
    print("%s ✔ {}%s".format(message) % (fg(2), attr(0)))

  def error(self, message):
    print("%s ✘ {}%s".format(message) % (fg(1), attr(0)))
