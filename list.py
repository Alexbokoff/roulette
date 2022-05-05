list_number = [18, 13, 20, 23, 29, 7, 29, 22, 14, 19, 26, 35, 9, 29,
               17, 23, 13, 28, 9, 0, 21, 21, 16, 10, 3, 24, 22, 33,
               0, 7, 28, 14, 8, 31, 2, 4, 36, 21, 20, 31, 21, 16, 10,
               6, 9, 20, 15, 24, 21, 36, 35, 12, 25, 12, 28, 31, 26,
               30, 14, 6, 6, 19, 19, 14, 25, 21, 31, 18, 19, 28, 15,
               20, 35, 32, 12, 22, 35, 30, 11, 5, 21, 32, 4, 8, 5, 20,
               3, 10, 6, 26, 2, 19, 6, 3, 10, 11, 15, 26, 14, 32, 22,
               9, 17, 27, 2, 0, 1, 2, 30, 29, 30, 4, 9, 12, 28, 3, 3,
               12, 7, 11, 32, 7, 2, 21, 11, 20, 20, 6, 5, 7, 10, 7, 20,
               35, 23, 28, 2, 14, 4, 16, 16, 22, 22, 9, 20, 4, 12, 15,
               17, 6, 26, 18, 19, 3, 14, 33, 26, 13, 20, 29, 33, 16, 26,
               10, 26, 7, 23, 23, 17, 1, 20, 33, 20, 26, 17, 11, 12, 14,
               9, 8, 29, 23, 14, 4, 7, 3, 17, 12, 4, 7, 5, 14, 13, 24, 31,
               21, 29, 12, 34, 28, 28, 11, 15, 12, 22, 36, 36, 9, 8, 17, 19,
               9, 28, 33, 2, 22, 9, 13, 23, 18, 1, 34, 8, 2, 35, 13, 10, 29,
               34, 35, 17, 36, 1, 27, 30, 25, 3, 20, 15, 33, 12, 26, 12, 26,
               29, 2, 19, 27, 29, 36, 29, 11, 26, 29, 24, 33, 24, 31, 12, 13,
               14, 28, 15, 0, 10, 0, 15, 12, 0, 26, 11, 11, 34, 12, 4, 3, 31,
               16, 28, 17, 25, 16, 6, 21, 15, 3, 9, 21, 7, 12, 10, 27, 9, 30,
               4, 0, 19, 1, 32, 24, 14, 4, 18, 13, 15, 36, 23, 34, 32, 36, 23,
               9, 7, 0, 32, 11, 3, 3, 33, 13, 19, 10, 27, 6, 6, 14, 35, 4, 18,
               26, 14, 33, 30, 9, 1, 19, 16, 27, 30, 4, 35, 4, 13, 33, 8, 13,
               14, 34, 1, 34, 7, 16, 29, 34, 19, 7, 32, 33, 33, 20, 9, 32, 11,
               5, 34, 17, 20, 35, 16, 34, 36, 20, 22, 32, 17, 5, 28, 0, 30, 24,
               28, 11, 15, 22, 36, 36, 9, 8, 17, 19, 9, 28, 33, 2, 22, 9, 13, 23,
               18, 1, 34, 35, 34, 35, 19, 29, 4, 30, 19, 20, 31, 31, 19, 29, 10,
               2, 30, 36, 27, 34, 21, 23, 36, 10, 14, 25, 28, 31, 0, 18, 3, 15, 13,
               25, 10, 10, 18, 31, 35, 22, 11, 12, 31, 26, 27, 0, 12, 30, 18, 2, 36,
               35, 33, 27, 33, 24, 22, 26, 13, 8, 17, 28, 4, 26, 8, 32, 17, 31, 8, 17,
               9, 15, 19, 14, 12, 28, 22, 1, 0, 30, 5, 5, 2, 24, 27, 36, 31, 26, 1, 30,
               2, 20, 9, 24, 13, 29, 13, 30, 24, 27, 18, 22, 7, 31, 6, 33, 1, 4, 36, 12,
               26, 7, 35, 22, 24, 29, 32, 35, 19, 22, 9, 20, 13, 12, 35, 19, 32, 21, 5, 1,
               29, 15, 23, 27, 36, 25, 1, 16, 31, 15, 17, 35, 8, 12, 30, 26, 35, 15, 9, 26,
               26, 15, 35, 16, 21, 2, 36, 29, 2, 10, 6, 4, 6, 22, 27, 0, 3, 25, 35, 22, 4, 2, 33,
               25, 33, 10, 19, 8, 7, 8, 30, 27, 36, 17, 27, 9, 32, 9, 13, 29, 3, 35, 34, 35, 19, 29,
               4, 30, 19, 20, 6, 22, 29, 16, 21, 22, 17, 30, 19, 20, 4, 18, 3, 10, 27, 5, 14, 32, 5, 31,
               36, 16, 23, 18, 21, 21, 22, 4, 6, 0, 23, 1, 0, 30, 25, 6, 35, 12, 31, 13, 28, 16, 5, 34,
               14, 4, 33, 0, 18, 21, 6, 8, 5, 0, 7, 7, 9, 0, 24, 35, 35, 16, 9, 7, 8, 14, 15, 0, 9, 1, 24,
               27, 2, 7, 32, 28, 35, 35, 9, 8, 28, 12, 30, 20, 4, 18, 15, 23, 27, 0, 12, 6, 33, 4, 1, 19, 7,
               35, 32, 16]

list_number2 = []
