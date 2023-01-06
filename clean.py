import pandas as pd
import ast

def read_from_csv(filename=""):
    df = pd.read_csv(filename)
    X = df["X"].tolist()
    Y = df["Y"].tolist()
    return X, Y

def write_to_csv(filename="translated.csv",X=[],Y=[]):
    result = pd.DataFrame({"X": X, "Y": Y})
    result.to_csv(filename)

def import_file(filename=""):
    #get filename
   # filename = input("Enter filename: ")
    #read from csv
    X, Y = read_from_csv(filename)
    return X, Y

def clean(X, Y):
    new_X = []
    new_Y = []
    for i in range(len(Y)):
        curr_y = ast.literal_eval(Y[i])
        curr_x = ast.literal_eval(X[i])

        x = []
        y = []
        for i in range(len(curr_x)):
            #check number of words 
            words = curr_x[i].split(" ")
            if(len(words) == 1):

                x.append(curr_x[i])
                y.append(curr_y[i])
            else:
                #get the label
                label = curr_y[i]

                for word in words:
                    x.append(word)

                    if(label == "O"):
                        #just append O
                        y.append(label)
                    elif(label[0] == "I"):
                        y.append("I-" + label[2:])
                    else:
                        #append B-<label>
                        y.append("B-" + label[2:])
                        label = "I-" + label[2:]
        new_X.append(x)
        new_Y.append(y)

    return new_X, new_Y




def main():
    filename = input("Enter filename: ")
    X, Y = import_file(filename)
    X, Y = clean(X, Y)
    write_to_csv(filename, X, Y)

if __name__ == "__main__":
    main()

