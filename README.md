# CustomDictionary
Just a custom dictionnary in python 

Spécifications:

Voici la liste des mécanismes que notre classe devra mettre en œuvre. Un peu plus bas, vous trouverez un exemple de manipulation de l'objet qui reprend ces spécifications :

    On doit pouvoir créer le dictionnaire de plusieurs façons :

        Vide : on appelle le constructeur sans lui passer aucun paramètre et le dictionnaire créé est donc vide.

        Copié depuis un dictionnaire : on passe en paramètre du constructeur un dictionnaire que l'on copie par la suite dans notre objet. On peut ainsi écrireconstructeur(dictionnaire)et les clés et valeurs contenues dans le dictionnaire sont copiées dans l'objet construit.

        Pré-rempli grâce à des clés et valeurs passées en paramètre : comme les dictionnaires usuels, on doit ici avoir la possibilité de pré-remplir notre objet avec des couples clés-valeurs passés en paramètre (constructeur(cle1 = valeur1, cle2 = valeur2, …)).

    Les clés et valeurs doivent être couplées. Autrement dit, si on cherche à supprimer une clé, la valeur correspondante doit également être supprimée. Les clés et valeurs se trouvant dans des listes de même taille, il suffira de prendre l'indice dans une liste pour savoir quel objet lui correspond dans l'autre. Par exemple, la clé d'indice0est couplée avec la valeur d'indice0.

    On doit pouvoir interagir avec notre objet conteneur grâce aux crochets, pour récupérer une valeur (objet[cle]), pour la modifier (objet[cle] = valeur) ou pour la supprimer (del objet[cle]).

    Quand on cherche à modifier une valeur, si la clé existe on écrase l'ancienne valeur, si elle n'existe pas on ajoute le couple clé-valeur à la fin du dictionnaire.

    On doit pouvoir savoir grâce au mot-cléinsi une clé se trouve dans notre dictionnaire (cle in dictionnaire).

    On doit pouvoir demander la taille du dictionnaire grâce à la fonctionlen.

    On doit pouvoir afficher notre dictionnaire directement dans l'interpréteur ou grâce à la fonctionprint. L'affichage doit être similaire à celui des dictionnaires usuels ({cle1: valeur1, cle2: valeur2, …}).

    L'objet doit définir les méthodessortpour le trier etreversepour l'inverser. Le tri de l'objet doit se faire en fonction des clés.

    L'objet doit pouvoir être parcouru. Quand on écritfor cle in dictionnaire, on doit parcourir la liste des clés contenues dans le dictionnaire.

    À l'instar des dictionnaires, trois méthodeskeys()(renvoyant la liste des clés),values()(renvoyant la liste des valeurs) etitems()(renvoyant les couples (clé, valeur)) doivent être mises en œuvre. Le type de retour de ces méthodes est laissé à votre initiative : il peut s'agir d'itérateurs ou de générateurs (tant qu'on peut les parcourir).

    On doit pouvoir ajouter deux dictionnaires ordonnés (dico1 + dico2) ; les clés et valeurs du second dictionnaire sont ajoutées au premier.
