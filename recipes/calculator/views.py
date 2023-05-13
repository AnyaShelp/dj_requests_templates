from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1}
    # можете добавить свои рецепты ;)
}


def omlet(request):
    servings = int(request.GET.get("servings", 1))
    for i in DATA['omlet']:
        DATA['omlet'][i] *= servings
    context = {
        'recipe': DATA['omlet'],
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)


def pasta(request):
    servings = int(request.GET.get("servings", 1))
    for i in DATA['pasta']:
        DATA['pasta'][i] *= servings
    context = {
        'recipe': DATA['pasta'],
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)


def buter(request):
    servings = int(request.GET.get("servings", 1))
    for i in DATA['buter']:
        DATA['buter'][i] *= servings
    context = {
        'recipe': DATA['buter'],
        'servings': servings
    }
    return render(request, 'calculator/index.html', context)
