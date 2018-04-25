# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render


# import poms.facetedbrowser.facetspecs as SPECS


##################
#  Wed Oct 13 16:18:19 BST 2010
#  Family Trees section:
#
##################


def familytrees(request, image_id):
    mappings = {'1': ['familytrees1.html', 'Scottishroyalfamily.capt.jpg'],
                '2': ['familytrees2.html', 'EarlDaviddescendants.jpg'],
                '3': ['familytrees3.html', 'Englishroyalfamily.jpg'],
                '4': ['familytrees4.html', 'Manxroyalfamily.jpg'],
                }

    # request.session['queryargs'] = []
    # request.session['activeIDs'] = []

    template_name = mappings[image_id][0]
    image_name = mappings[image_id][1]

    return render(request,
                  'pomsapp/familytrees/' + template_name,
                  {
                      'permalink': request.get_host() + request.path,
                      'FAMTREE_IMAGE': image_name,
                      'image_id': image_id,
                  }
                  )


def familytrees_home(request):
    return HttpResponseRedirect("1")
