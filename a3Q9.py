        # # # # #   
      # # # # #
    # # # # #
  # # # # #
# # # # #
st=5
for a in range(5):
    for b in range(5+st):
        if b>=5-a-1 and b<5-a-1+st:
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()