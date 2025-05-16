def print_umanga():
    # Define patterns for each letter
    letters = {
    "U": ["*      *",
          "*      *",
          "*      *",
          "*      *",
          "********"],

    "M": ["*       *",
          "* *   * *",
          "*   *   *",
          "*       *",
          "*       *"],

    "A": ["     *    ",
          "    * *   ",
          "   *****  ",
          "  *     * ",
          " *       *"],

    "N": ["*     *",
          "* *   *",
          "*  *  *",
          "*   * *",
          "*    **"],

    "G": ["       ***   ",
          "    *        ",
          " *      *****",
          "    *   *   *",         
          "        *   *"],

    "A": ["     *    ",
          "    * *   ",
          "   *****  ",
          "  *     * ",
          " *       *"]
}

    # Sequence of letters in the name
    name = ['U', 'M', 'A', 'N', 'G', 'A']

    
    # Print each row of the pattern
    for row in range(7):
        line = ''
        for letter in name:
            line += letters[letter][row] + '  '
        print(line)

print_umanga()

               


