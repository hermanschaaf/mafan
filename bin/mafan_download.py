from mafan import download_data

if __name__ == '__main__':
  confirm = raw_input("You are about to download all dictionary files. Could be up to 50MB in total. Are you sure?\n (y/n) ")
  if confirm == 'y' or confirm == 'yes':
      download_data.download_traditional_word_list()