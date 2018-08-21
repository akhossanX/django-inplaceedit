# -*- coding: utf-8 -*-
# Copyright (c) 2010-2013 by Yaco Sistemas <goinnn@gmail.com>
#               2015 by Pablo Martín <goinnn@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.

from django.shortcuts import render, get_object_or_404

from testing.inplace_transmeta.models import News


def news_index(request):
    return render(request, 'news/index.html', {'news': News.objects.all()})


def news_edit(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/edit.html', {'news_item': news_item})
