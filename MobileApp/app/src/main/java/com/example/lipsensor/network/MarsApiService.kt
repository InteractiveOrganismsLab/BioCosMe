package com.example.lipsensor.network

import com.example.lipsensor.model.MarsPhoto
import com.example.lipsensor.model.PredictionResponse
import retrofit2.Retrofit
import com.jakewharton.retrofit2.converter.kotlinx.serialization.asConverterFactory
import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import retrofit2.http.GET
import retrofit2.http.POST
import retrofit2.Response
import okhttp3.MultipartBody
import retrofit2.http.Multipart
import retrofit2.http.Part

private const val BASE_URL =
//    "https://android-kotlin-fun-mars-server.appspot.com"
//    "http://10.0.2.2:5000/"
  "http://127.0.0.1:5000"

/**
 * Use the Retrofit builder to build a retrofit object using a kotlinx.serialization converter
 */
private val retrofit = Retrofit.Builder()
    .addConverterFactory(Json.asConverterFactory("application/json".toMediaType()))
    .baseUrl(BASE_URL)
    .build()

/**
 * Retrofit service object for creating api calls
 */
interface MarsApiService {

    @GET("photos")
    suspend fun getPhotos(): List<MarsPhoto>
    @Multipart
    @POST("predict")
    suspend fun sendPhotos(@Part filePart: MultipartBody.Part): Response<PredictionResponse>
}

/**
 * A public Api object that exposes the lazy-initialized Retrofit service
 */
object MarsApi {
    val retrofitService: MarsApiService by lazy {
        retrofit.create(MarsApiService::class.java)
    }
}