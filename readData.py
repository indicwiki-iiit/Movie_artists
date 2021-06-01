import pickle
import pandas as pd



def main():
	moviesFile = './oscar2k.csv'
	moviesDF = pd.read_csv(moviesFile)
	# moviesDF = clean(moviesDF)

	pickle.dump(moviesDF, open('./oscar2k.pkl', 'wb'))


if __name__ == '__main__':
	main()
 

    
