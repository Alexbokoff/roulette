list_number = [3, 4, 17, 34, 36, 0, 28, 30, 34, 13, 7, 26, 10, 11, 26, 27, 20, 27, 9, 22, 30, 20, 3, 17, 2, 13,
               14, 31, 26, 12, 18, 34, 23, 17, 12, 23, 4, 4, 9, 12, 13, 0, 21, 27, 14, 16, 15, 11, 9, 12, 29, 21,
               14, 9, 23, 18, 10, 24, 32, 9, 26, 23, 9, 36, 27, 28, 9, 22, 4, 20, 24, 8, 5, 17, 15, 8, 16, 27, 20,
               34, 36, 36, 15, 35, 17, 26, 4, 36, 30, 35, 20, 11, 23, 36, 5, 11, 7, 28, 19, 19, 16, 32, 35, 7, 19,
               1, 4, 33, 6, 12, 0, 27, 23, 15, 18, 4, 20, 30, 12, 28, 8, 9, 35, 35, 28, 32, 7, 2, 27, 24, 1, 9, 0,
               15, 14, 8, 7, 9, 16, 35, 35, 24, 0, 9, 7, 7, 0, 5, 8, 6, 21, 18, 0, 33, 4, 14, 34, 5, 16, 28, 13, 31,
               12, 35, 6, 25, 30, 0, 1, 23, 0, 6, 4, 22, 21, 21, 18, 23, 16, 36, 31, 5, 32, 14, 5, 27, 10, 3, 18, 4,
               20, 19, 30, 17, 22, 21, 16, 29, 22, 6, 20, 19, 30, 4, 29, 19, 35, 34, 35, 3, 29, 13, 9, 32, 9, 27, 17,
               36, 27, 30, 8, 7, 8, 19, 10, 33, 25, 33, 2, 4, 22, 35, 25, 3, 0, 27, 22, 6, 4, 6, 10, 2, 29, 36, 2, 21,
               16, 35, 15, 26, 26, 9, 15, 35, 26, 30, 12, 8, 35, 17, 15, 31, 16, 1, 25, 36, 27, 23, 15, 29, 1, 5, 21,
               32, 19, 35, 12, 13, 20, 9, 22, 19, 35, 32, 29, 24, 22, 35, 7, 26, 12, 36, 4, 1, 33, 6, 31, 7, 22, 18, 27,
               24, 30, 13, 29, 13, 24, 9, 20, 2, 30, 1, 26, 31, 36, 27, 24, 2, 5, 5, 30, 0, 1, 22, 28, 12, 14, 19, 15,
               9, 17, 8, 31, 17, 32, 8, 26, 4, 28, 17, 8, 13, 26, 22, 24, 33, 27, 33, 35, 36, 2, 18, 30, 12, 0, 27, 26,
               31, 12, 11, 22, 35, 31, 18, 10, 10, 25, 13, 15, 3, 18, 0, 31, 28, 25, 14, 10, 36, 23, 21, 34, 27, 36, 30,
               2, 10, 29, 19, 31, 31, 20, 19, 30, 4, 29, 19, 35, 34, 35, 34, 1, 18, 23, 13, 9, 22, 2, 33, 28, 9, 19, 17,
               8, 9, 36, 36, 22, 15, 11, 28, 24, 30, 0, 28, 5, 17, 32, 22, 20, 36, 34, 16, 35, 20, 17, 34, 5, 11, 32, 9,
               20, 33, 33, 32, 7, 19, 34, 29, 16, 7, 34, 1, 34, 14, 13, 8, 33, 13, 4, 35, 4, 30, 27, 16, 19, 1, 9, 30,
               33, 14, 26, 18, 4, 35, 14, 6, 6, 27, 10, 19, 13, 33, 3, 3, 11, 32, 0, 7, 9, 23, 36, 32, 34, 23, 36, 15,
               13, 18, 4, 14, 24, 32, 1, 19, 0, 4, 30, 9, 27, 10, 12, 7, 21, 9, 3, 15, 21, 6, 16, 25, 17, 28, 16, 31, 3,
               4, 12, 34, 11, 11, 26, 0, 12, 15, 0, 10, 0, 15, 28, 14, 13, 12, 31, 24, 33, 24, 29, 26, 11, 29, 36, 29,
               27, 19, 2, 29, 26, 12, 26, 12, 33, 15, 20, 3, 25, 30, 27, 1, 36, 17, 35, 34, 29, 10, 13, 35, 2, 8, 34, 1,
               18, 23, 13, 9, 22, 2, 33, 28, 9, 19, 17, 8, 9, 36, 36, 22, 12, 15, 11, 28, 28, 34, 12, 29, 21, 31, 24,
               13, 14, 5, 7, 4, 12, 17, 3, 7, 4, 14, 23, 29, 8, 9, 14, 12, 11, 17, 26, 20, 33, 20, 1, 17, 23, 23, 7, 26,
               10, 26, 16, 33, 29, 20, 13, 26, 33, 14, 3, 19, 18, 26, 6, 17, 15, 12, 4, 20, 9, 22, 22, 16, 16, 4, 14, 2,
               28, 23, 35, 20, 7, 10, 7, 5, 6, 20, 20, 11, 21, 2, 7, 32, 11, 7, 12, 3, 3, 28, 12, 9, 4, 30, 29, 30, 2,
               1, 0, 2, 27, 17, 9, 22, 32, 14, 26, 15, 11, 10, 3, 6, 19, 2, 26, 6, 10, 3, 20, 5, 8, 4, 32, 21, 5, 11,
               30, 35, 22, 12, 32, 35, 20, 15, 28, 19, 18, 31, 21, 25, 14, 19, 19, 6, 6, 14, 30, 26, 31, 28, 12, 25, 12,
               35, 36, 21, 24, 15, 20, 9, 6, 10, 16, 21, 31, 20, 21, 36, 4, 2, 31, 8, 14, 28, 7, 0, 33, 22, 24, 3, 10,
               16, 21, 21, 0, 9, 28, 13, 23, 17, 29, 9, 35, 26, 19, 14, 22, 29, 7, 29, 23, 20, 13, 18, 25, 9, 12, 22,
               24, 2, 35, 32, 0, 3, 12, 20, 11, 25, 19, 3, 25, 18, 10, 20, 15, 7, 9, 0, 31, 14, 5, 27, 22, 7, 29, 21,
               16, 16, 23, 0, 31, 31, 5, 36, 15, 0, 19, 17, 7, 31, 26, 23, 16, 7, 30, 35, 19, 32, 23, 23, 4, 4, 2, 18,
               11, 0, 0, 3, 32, 36, 35, 19, 31, 12, 16, 33, 31, 36, 29, 15, 27, 19, 30, 17, 21, 22, 9, 0, 7, 9, 4, 21,
               26, 34, 34, 7, 24, 19, 25, 29, 17, 15, 27, 27, 14, 19, 1, 0, 1, 12, 21, 15, 20, 18, 29, 7, 18, 2, 36, 2,
               20, 15, 16, 28, 28, 18, 11, 11, 27, 32, 30, 7, 17, 21, 19, 2, 8, 3, 24, 19, 30, 6, 18, 34, 5, 11, 13, 32,
               22, 18, 36, 12, 3, 24, 32, 4, 11, 25, 10, 14, 22, 25, 14, 15, 23, 22, 11, 34, 17, 23, 33, 16, 9, 5, 6, 0,
               19, 12, 15, 7, 3, 9, 27, 35, 31, 13, 30, 9, 23, 25, 31, 11, 24, 30, 33, 6, 2, 30, 12, 32, 29, 35, 28, 27,
               17, 12, 10, 34, 16, 8, 20, 18, 25, 29, 24, 28, 9, 6, 17, 14, 8, 14, 14, 7, 12, 19, 33, 0, 32, 17, 5, 7,
               5, 7, 7, 5, 14, 14, 32, 17, 23, 27, 36, 36, 19, 31, 1, 24, 9, 17, 12, 30, 10, 6, 3, 3, 15, 0, 30, 35, 23,
               4, 31, 23, 13, 15, 29, 13, 34, 30, 16, 12, 29, 35, 32, 18, 30, 19, 33, 22, 20, 30, 36, 17, 15, 20, 3, 22,
               7, 5, 19, 29, 16, 27, 28, 29, 21, 17, 12, 21, 36, 19, 33, 3]

list_number2 = []
