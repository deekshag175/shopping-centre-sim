class converter:
    def is_integer(self, n):
        try:
            int(n)
        except ValueError:
            return False
        else:
            return True
 
  