from proxy import proxy, HttpResponse


def func(req):
    if 's' not in req.args:
        return HttpResponse('', code=400)

    return HttpResponse(req.args['s'])


main = proxy(func)
