# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render


# import poms.facetedbrowser.facetspecs as SPECS


##################
#  Wed Oct 13 16:18:19 BST 2010
#  Family Trees section:
#
##################


def familytrees(request, image_id='1'):
    mappings = {'1': 'Scottishroyalfamily.capt.jpg',
                '2': 'EarlDaviddescendants.jpg',
                '3': 'Englishroyalfamily.jpg',
                '4': 'Manxroyalfamily.jpg',
                }


    image_name = mappings[image_id]

    return render(request,
                  'pomsapp/familytrees/familytrees.html',
                  {
                      'permalink': request.get_host() + request.path,
                      'FAMTREE_IMAGE': 'images/famtree/'+image_name,
                      'image_id': image_id,
                  }
                  )


def familytrees_home(request):
    return HttpResponseRedirect("1")
