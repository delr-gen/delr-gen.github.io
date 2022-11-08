class Recipe:

    def __init__(self, name):
        self.recipeName = ""
        self.ingredients = {}
        self.steps = []
    
    def getName(self):
        return self.recipeName

    def addIngredient(self, ingredient, amount=None):
        self.ingredients[ingredient] = amount
    
    def removeIngredient(self, ingredient):
        if ingredient in self.ingredients:
            del self.ingredients[ingredient]

    def getIngredients(self):
        return self.ingredients.items()
    
    def addStep(self, step, location=None):
        if location!= None:
            if 0 <= location < len(self.steps):
                self.steps = self.steps[0:location] + [step] + self.steps[location:]
            elif location == len(self.steps):
                self.steps.append(step)
        else:
            self.steps.append(step)

    def removeStep(self, stepNum):
        if 0 <= stepNum < len(self.steps):
            self.steps.pop(stepNum)
    
    def moveStep(self, before, after):
        if 0 <= before < len(self.steps) and 0 <= after < len(self.steps):
            self.steps[before], self.steps[after] = self.steps[after], self.steps[before]
        
    def getSteps(self):
        return self.steps
