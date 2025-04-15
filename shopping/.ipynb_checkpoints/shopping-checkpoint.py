import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    import csv
    evidencia = []
    label = []
    diccionarioColumnas = {"Administrative" : int,
                           "Administrative_Duration" : float,
                           "Informational" : int,
                           "Informational_Duration" : float,
                           "ProductRelated" : int,
                           "ProductRelated_Duration" : float,
                           "BounceRates" : float,
                           "ExitRates" : float,
                           "PageValues" : float,
                           "SpecialDay" : float,
                           "Month" : "mes" ,
                           "OperatingSystems": int,
                           "Browser" : int,
                           "Region" : int,
                           "TrafficType" : int,
                           "VisitorType" : "visitante",
                           "Weekend" : "finde",
                           "Revenue" : "label",
                          }
    diccionarioMeses = {
                            "Jan": 0, "Feb": 1, "Mar": 2, "Apr": 3,
                            "May": 4, "June": 5, "Jul": 6, "Aug": 7,
                            "Sep": 8, "Oct": 9, "Nov": 10, "Dec": 11
}


    with open("shopping.csv") as f:  ## Verificar el orden del pack y unpack o va ser GG sse ya morning
        reader = csv.reader(f)   ## Posiblemente en el check50 va lanzar errores de validaciónes o datos vacios, who knows
        encabezado = next(reader)
        for row in reader:
            fila = []
            for nombre_columna, valor in zip(encabezado[:-1], row[:-1]):
                tipos = diccionarioColumnas[nombre_columna]

                if tipos == int:
                    fila.append(int(valor))
                elif tipos == float:
                    fila.append(float(valor))
                elif tipos == "finde":
                    if valor.strip().lower() == "true":
                        fila.append(1)
                    else:
                        fila.append(0)
                elif tipos == "mes":
                    fila.append(diccionarioMeses[valor])
                elif tipos == "visitante":
                    if valor.strip().lower() == "returning_visitor":
                        fila.append(1)
                    else:
                        fila.append(0)
                        
            evidencia.append(fila)
            label.append(1 if row[-1].strip().lower() == "true" else 0)

    return (evidencia, label)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """

    neigh = KNeighborsClassifier(n_neighbors = 1)
    trainingX = [row for row in evidence]
    trainingY = [row for row in labels]
    
    neigh.fit(trainingX, trainingY)

    return neigh


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    truePositive = 0 ## True 
    labelPositive = 0
    trueNegative = 0
    labelNegative = 0

    for label, prediccion in zip(labels, predictions):
        if label == 0:
            labelNegative += 1
        else:
            labelPositive += 1
            
        if label == 0 and prediccion == 0:
            trueNegative +=1
        
        elif label == 1 and prediccion == 1:
            truePositive += 1

    print("Positivos: ", truePositive)
    print("Negativos: ", trueNegative)
    ratePositive = truePositive / labelPositive if labelPositive else 0
    rateNegative = trueNegative / labelNegative if labelNegative else 0

    return (ratePositive, rateNegative)


















    


if __name__ == "__main__":
    main()
