package com.example.arthur.agrosale;


import android.os.AsyncTask;

import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class DownloadConteudo extends AsyncTask<URL,Void, ArrayList>
{
    //Metodo que executa a Thread em segundo plano
    @Override
    protected ArrayList<Produto> doInBackground(URL...urls) {
        OkHttpClient client = new OkHttpClient();
        Gson gson = new Gson();
        ArrayList<Produto> listaProdutos= new ArrayList();

        Request request = new Request.Builder().url(urls[0]).build();

        try {
            Response response = client.newCall(request).execute();

            String json= response.body().string();
            listaProdutos= gson.fromJson(json,new TypeToken<ArrayList<Carro>>(){}.getType());


        } catch (IOException e) {
            e.printStackTrace();
        }
        return listaProdutos;
    }

    //Metodo que executa apos a conclusao da Thread
    //Codigo chamado ja na tread principal
    public void onPostExecute(ArrayList<Produto> produtos)
    {



    }

}
