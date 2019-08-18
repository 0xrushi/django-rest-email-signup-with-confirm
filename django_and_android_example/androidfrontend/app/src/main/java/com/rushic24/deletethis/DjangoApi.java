package com.rushic24.deletethis;

import okhttp3.RequestBody;
import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.POST;

public interface DjangoApi {

    String DJANGO_SITE = "http://192.168.1.104:8000/post/";


    @POST("create/")
    Call<RequestBody> addPostVoditel(@Body PostModel postModel);



}